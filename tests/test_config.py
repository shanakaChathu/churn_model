from app import form_response 

class  NotANumber(Exception):
    def __init__(self, message="Values entered are not Numerical"):
        self.message = message
        super().__init__(self.message)

input_data = {
    "incorrect_values": 
    {"number_vmail_messages": 3, 
    "total_day_calls": 4, 
    "total_eve_minutes": 'as', 
    "total_eve_charge": 12, 
    "total_intl_minutes": 1, 
    "number_customer_service_calls": 'ab', 
    },

    "correct_values": 
    {"number_vmail_messages": 3, 
    "total_day_calls": 4, 
    "total_eve_minutes": 2, 
    "total_eve_charge": 12, 
    "total_intl_minutes": 1, 
    "number_customer_service_calls": 4, 
    }
}

def test_form_response_incorrect_values(data=input_data["incorrect_values"]):
    res=form_response(data)
    assert res == NotANumber().message

