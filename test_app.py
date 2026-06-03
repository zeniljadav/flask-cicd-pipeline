from app import devops_message

def test_devops_message():
    # This checks if our python function returns exactly what we expect
    assert devops_message() == "CI/CD Pipeline is Working!"