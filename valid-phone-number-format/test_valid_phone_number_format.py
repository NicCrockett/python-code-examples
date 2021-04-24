from datetime import datetime
from pathlib import Path
from valid_phone_number_format import validNumber

def test_validNumber():
	strTestsFile = Path('test_samples.txt')
	strResultsFile = Path('test_results.txt')
	strDateTime = datetime.now()

	with open(strTestsFile, 'r') as fileTests:
		with open(strResultsFile, 'a+', newline = '') as fileResults:
			fileResults.write('\nTest results run on ' + strDateTime.strftime('%Y-%m-%d') + ' at ' + strDateTime.strftime('%I.%M.%S %p') + '\n')
			for i in fileTests:
				currentline = i.split(',')
				strPassFail = 'Pass' if eval(currentline[1]) == validNumber(currentline[0]) else 'Fail'
				fileResults.write('Test Phone Number: {} - Test Results: {} - Expected Results: {} - Pass or Fail: {}\n'.format(currentline[0], validNumber(currentline[0]), currentline[1].replace('\n', ''), strPassFail))
