from .context import preflightpy as pre

class TestEnvUpdate:

    def test_pressure(self):
        environment = pre.Environment( [113, 0.01, 9.80665, 0.02896968, 8.314462618, 1.4, 101325] )
        environment.get_status(5000)
        assert round(environment.P, -1) == 54040
        environment.get_status(11019)
        assert round(environment.P, -1) == 22630
        environment.get_status(20000)
        assert round(environment.P, -1) == 5530
        environment.get_status(70000)
        assert round(environment.P, 1) == 5.2

    def test_temperature(self):
        environment = pre.Environment( [113, 0.01, 9.80665, 0.02896968, 8.314462618, 1.4, 101325] )
        environment.get_status(5000)
        assert round(environment.T, 2) == 255.68
        environment.get_status(20063)
        assert round(environment.T, 2) == 216.65
        environment.get_status(30000)
        assert round(environment.T, 2) == 226.51
        environment.get_status(47350)
        assert round(environment.T, 2) == 270.65
        environment.get_status(71802)
        assert round(environment.T, 2) == 214.64

    def test_density(self):
        environment = pre.Environment( [113, 0.01, 9.80665, 0.02896968, 8.314462618, 1.4, 101325] )
        environment.get_status(5000)
        assert round(environment.Rho, 4) == 0.7365
        environment.get_status(11019)
        assert round(environment.Rho, 4) == 0.3639
        environment.get_status(20063)
        assert round(environment.Rho, 4) == 0.0880
        environment.get_status(40000.0)
        assert round(environment.Rho, 4) == 0.0040


    def test_speed_of_sound(self):
        environment = pre.Environment( [113, 0.01, 9.80665, 0.02896968, 8.314462618, 1.4, 101325] )
        environment.get_status(1000)
        assert round(environment.c, 1) == 336.4
        environment.get_status(10000)
        assert round(environment.c, 1) == 299.5
        environment.get_status(30000)
        assert round(environment.c, 1) == 301.7
