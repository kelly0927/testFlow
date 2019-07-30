import allure, pytest


class Test_Abc:
    def setup(self):
        pass

    def teardown(self):
        pass
    @allure.issue("http://www.163.com")
    @allure.testcase("http://www.baidu.com/test_001")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_al(self):
        assert 0
    @allure.step(title="第一个测试开启了啊")
    def test_success(self):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert 1
if __name__ == '__main__':
    # pytest.main(['-s', 'test_001.py'])
    pytest.main(['-s','--alluredir report test_001.py'])

    # pytest.main("-s --alluredir report test_001.py")