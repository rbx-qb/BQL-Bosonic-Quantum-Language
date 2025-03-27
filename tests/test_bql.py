from src.bql.interpreter import BQLInterpreter

def test_create_register():
    bql = BQLInterpreter()
    bql.execute("CREATE q1 4")
    assert "q1" in bql.registers
    assert bql.registers["q1"]["levels"] == 4

def test_entangle():
    bql = BQLInterpreter()
    bql.execute("CREATE q1 4")
    bql.execute("CREATE q2 4")
    bql.execute("ENTANGLE q1 q2")

