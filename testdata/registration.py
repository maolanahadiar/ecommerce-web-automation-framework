from utils.data_generator import DataGenerator

REGISTRATION_DATA = {
    "valid": {
        "username" : DataGenerator.username(),
        "password" : DataGenerator.password(),
        "expected_message" : "Sign up successful."
        },
    "invalid": {
        "username" : "redgery25",
        "password" : DataGenerator.password(),
        "error_message" : "This user already exist."
        }
}