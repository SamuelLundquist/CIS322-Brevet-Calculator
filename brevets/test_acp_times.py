from acp_times import open_time
from acp_times import close_time
import arrow

time = '2019-01-01T00:00:00+00:00'

def test_open_time_string():
	assert open_time(100,200,'a random string') == ""

def test_close_time_string():
	assert close_time(100,200,'a random string') == ""

def test_open_time_long_dist():
	assert open_time(300,200,time) == ""
	assert open_time(500,400,time) == ""
	assert open_time(800,600,time) == ""
	assert open_time(1250,1000,time) == ""

def test_close_time_long_dist():
	assert close_time(300,200,time) == ""
	assert close_time(500,400,time) == ""
	assert close_time(800,600,time) == ""
	assert close_time(1250,1000,time) == ""

def test_open_time_200():
	assert open_time(0, 200, time) == "2019-01-01 00:00:00+00:00"
	assert open_time(60, 200, time) == "2019-01-01 01:46:00+00:00"
	assert open_time(120, 200, time) == "2019-01-01 03:32:00+00:00"
	assert open_time(175, 200, time) == "2019-01-01 05:09:00+00:00"
	assert open_time(205, 200, time) == "2019-01-01 05:53:00+00:00"

def test_close_time_200():
	assert close_time(0, 200, time) == "2019-01-01 01:00:00+00:00"
	assert close_time(60, 200, time) == "2019-01-01 04:00:00+00:00"
	assert close_time(120, 200, time) == "2019-01-01 08:00:00+00:00"
	assert close_time(175, 200, time) == "2019-01-01 11:40:00+00:00"
	assert close_time(205, 200, time) == "2019-01-01 13:30:00+00:00"

def test_open_time_300():
	assert open_time(0, 300, time) == "2019-01-01 00:00:00+00:00"
	assert open_time(60, 300, time) == "2019-01-01 01:46:00+00:00"
	assert open_time(120, 300, time) == "2019-01-01 03:32:00+00:00"
	assert open_time(175, 300, time) == "2019-01-01 05:09:00+00:00"
	assert open_time(200, 300, time) == "2019-01-01 05:53:00+00:00"
	assert open_time(275, 300, time) == "2019-01-01 08:14:00+00:00"
	assert open_time(320, 300, time) == "2019-01-01 09:00:00+00:00"

def test_close_time_300():
	assert close_time(0, 300, time) == "2019-01-01 01:00:00+00:00"
	assert close_time(60, 300, time) == "2019-01-01 04:00:00+00:00"
	assert close_time(120, 300, time) == "2019-01-01 08:00:00+00:00"
	assert close_time(175, 300, time) == "2019-01-01 11:40:00+00:00"
	assert close_time(200, 300, time) == "2019-01-01 13:20:00+00:00"
	assert close_time(275, 300, time) == "2019-01-01 18:20:00+00:00"
	assert close_time(320, 300, time) == "2019-01-01 20:00:00+00:00"
