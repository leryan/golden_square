from lib.reminder import Reminder

def test_reminds_user ():
    reminder = Reminder("Ryan")
    reminder.remind_me_to("Turn off computer")
    result = reminder.remind()
    assert result == "Turn off computer, Ryan!"