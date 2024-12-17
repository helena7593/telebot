from doctors.super_class import Dentist, Cardiologist

def test_doctor_booking_via_subclass():
    dentist = Dentist()
    assert dentist.name == "Dentist"
    assert dentist.schedule == ["10:00", "11:00", "12:00"]

def test_doctor_time():
    dentist = Dentist()
    assert dentist.book_time("10:00") == True
    assert "10:00" not in dentist.schedule

def test_doctor_time1():
    dentist = Dentist()
    assert dentist.book_time("10:00") == True

def test_doctor_time2():
    dentist = Dentist()
    assert dentist.book_time("13:00") == False

def test_doctor_time3():
    cardiologist = Cardiologist()
    assert cardiologist.name == "Cardiologist"

def test_doctor_time4():
    cardiologist = Cardiologist()
    assert cardiologist.schedule == ["16:00", "17:00", "18:00"]

def test_doctor_time5():
    cardiologist = Cardiologist()
    assert cardiologist.book_time("17:00") == True
    assert "17:00" not in cardiologist.schedule
