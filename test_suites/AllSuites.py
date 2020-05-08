import os
import unittest
import HtmlTestRunner
from tc_one.LoginTest import LoginTest
from tc_one.SignupTest import SignupTest
from tc_two.CreditTest import CreditTest
from tc_two.DebitTest import DebitTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(CreditTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(DebitTest)

# create test suite
sanityTestSuite = unittest.TestSuite([tc1, tc2])
functionalTestSuite = unittest.TestSuite([tc3, tc4])
unittest.TextTestRunner(verbosity=2).run(functionalTestSuite)

dir = os.getcwd()
outfile = open(dir + "SanityTestReport.html", "w")
runner = HtmlTestRunner.HTMLTestRunner(stream=outfile, verbosity=2)
runner.run(sanityTestSuite)

