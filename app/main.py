import enum
from io import BytesIO
import pandas as pd
from fastapi import FastAPI, File, HTTPException
from pydantic import BaseModel

from app.models import DepositLinearModel, DepositDecisionTree, DepositLogisticDecision

app = FastAPI()
models_path = {
  'linear': (DepositLinearModel, 'app/resource/linear_model.pickle'),
  'decision_tree': (DepositDecisionTree, 'app/resource/decision_tree.pickle'),
  'logistic': (DepositLogisticDecision, 'app/resource/decision_logistic.pickle')
}
columns = [
  'age', 'balance', 'campaign', 'day', 'duration', 'pdays', 'previous'
]
models = {}


class ModelEnum(str, enum.Enum):
  linear = 'linear'
  decision_tree = 'decision tree'
  logistic = 'logistic'


class Prediction(BaseModel):
  prediction: str
  probabilitie: str


@app.on_event("startup")
def load_models():
  for model_name, (model_type, model_checkpoint) in models_path.items():
    new_model = model_type()
    new_model.load(model_checkpoint)
    models[model_name] = new_model


@app.get("/")
def root():
  return {"message": "Hello! Application is running"}


@app.post("/predict/")
async def predict(model_name: ModelEnum, file: bytes = File()) -> list[Prediction]:
  if model_name not in models:
    raise HTTPException(status_code=400, detail='Unknown model')

  model = models[model_name.name]

  try:
    data = pd.read_csv(BytesIO(file))
    data = data.reindex(sorted(data.columns), axis=1)
    assert list(data.columns) == columns
  except:
    raise HTTPException(status_code=400, detail='Incorrect file format')

  try:
    predictions = model.predict(data).tolist()
    probabilities = model.predict_proba(data)[:, 1].tolist()
    prediction_list = []
    for i in predictions:
      prediction_list.append(
          Prediction(prediction=predictions[i], probabilitie=probabilities[i]))
  except:
    raise HTTPException(status_code=500, detail='Internal server error')

  return prediction_list
