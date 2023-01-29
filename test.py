from main import P2PApp
Unit tests
def test_p2p_app():
    app = P2PApp()
    
    # Add users and check if they exist
    userA = app.add_user("User A")
    assert userA.name == "User A"
    assert app.get_user("User A") == userA
    
    userB = app.add_user("User B")
    assert userB.name == "User B"
    assert app.get_user("User B") == userB
    
    # Test depositing money
    userA.deposit(10)
    assert userA.check_balance() == 10
    
    userB.deposit(20)
    assert userB.check_balance() == 20
    
    # Test sending money
    assert userB.send_money(userA, 15) == True
    assert userA.check_balance() == 25
    assert userB.check_balance() == 5
    
    # Test checking balance
    assert userA.check_balance() == 25
    assert userB.check_balance() == 5
    
    # Test transferring money
    assert userA.transfer_money(25) == True
    assert userA.check_balance() == 0
    
    print("All tests pass.")
    
test_p2p_app()
