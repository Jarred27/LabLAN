import pyvisa as visa
scopeID='USB::0x0699::0x0368::C018240::INSTR'
awgID='USB::0x0699::0x0347::C030997::INSTR'

rm=visa.ResourceManager()
scope=rm.open_resource(scopeID)
awg=rm.open_resource(awgID)

scope.write('DIS:FORM XY')
scope.write('CH1:SCA 1.0E0')
scope.write('CH2:SCA 1.0E0')
awg.write('SOUR1:FREQ:MODE CW')
awg.write('SOUR1:FUNC:SHAP RAMP')
awg.write('SOUR1:FUNC:RAMP:SYMM 100')
awg.write('SOUR1:VOLT:LEV:IMM:HIGH 1V')
awg.write('SOUR1:VOLT:LEV:IMM:LOW -1V')
awg.write('OUTP1:STAT ON')
awg.write('SOUR2:FREQ:MODE CW')
awg.write('SOUR2:FUNC:SHAP SINE')
awg.write('SOUR2:VOLT:LEV:IMM:HIGH 2V')
awg.write('SOUR2:VOLT:LEV:IMM:LOW -2V')
awg.write('OUTP2:STAT ON')
