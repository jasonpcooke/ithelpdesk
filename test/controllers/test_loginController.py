from main.controllers.loginController import loginController

def test_invalidLogin():
    # Given
    users =[['correct@email.com', 'correctPassword1']]
    user = ['incorrect@email.com', 'incorrectPassword1']

    # When
    result = loginController.checkLoginDetails(users,user)

    # Then
    assert result == False

def test_validLogin():
    # Given
    users =[['correct@email.com', 'correctPassword1']]
    user = ['correct@email.com', 'correctPassword1']

    # When
    result = loginController.checkLoginDetails(users,user)

    # Then
    assert result == True