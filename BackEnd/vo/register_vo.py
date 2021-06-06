from dataclasses import dataclass

@dataclass(frozen=True)
class RegisterVO:
  access_token:str
  refresh_token:str

  def serialize_data(self):
    return{
      'access_token':self.access_token,
      'refresh_token':self.refresh_token
    }