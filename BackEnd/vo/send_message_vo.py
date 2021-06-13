from dataclasses import dataclass

@dataclass(frozen=True)
class SendMessageVO:
  message:str

  def serialize_data(self):
    return{
      'message':self.message,
    }