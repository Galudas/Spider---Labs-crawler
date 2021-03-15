import sys

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


ELEM = 'unselectedrow'
ZIP = '.c8 td:nth-child(2) a'


def get_students_names(file: str):
	f = open(file, "r")
	students = f.readlines()
	return [student.replace("\n", "") for student in students]


def create_options_selenium():
	options = Options()
	options.headless = True
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	options.add_experimental_option("prefs",
	                                {"download.default_directory": r"labs", "download.prompt_for_download": False,
	                                 "download.directory_upgrade": True, "safebrowsing.enabled": True})
	return options


def get_labs(link: str, u: str, p: str):
	students = get_students_names("students")

	driver = webdriver.Chrome(executable_path='./chromedriver',options=create_options_selenium())

	pageNr = 0
	savedElem = []
	driver.get("https://curs.upb.ro/my/")
	print(bcolors.BOLD + "==== Start Getting Labs with SPIDER ====")
	driver.find_element_by_id("username").send_keys(u)
	driver.implicitly_wait(2)
	driver.find_element_by_id("password").send_keys(p)
	driver.implicitly_wait(2)
	driver.find_element_by_id("loginbtn").click()
	driver.implicitly_wait(2)
	print(bcolors.OKCYAN + "Logged In")
	while True:
		driver.get(link + pageNr.__str__())
		driver.implicitly_wait(2)
		elements = driver.find_elements_by_css_selector(".unselectedrow")
		if len(elements) == 0:
			break
		savedElem.append(elements)
		pageNr += 1
		save_elems = []
		for elem in elements:
			name = elem.find_element_by_css_selector(".c2").text
			if name in students:
				save_elems.append((elem, name))
		for save_elem in save_elems:
			t = save_elem[0].find_elements_by_css_selector(ZIP)
			if len(t) > 0:
				driver.get(t[0].get_attribute("href"))
				print(bcolors.OKGREEN + save_elem[1], " lab downloaded")
			else:
				print(bcolors.FAIL + save_elem[1], " didn't uploaded the lab")
	print(bcolors.ENDC + "All .zip files are downloaded")


if __name__ == '__main__':
	get_labs('https://curs.upb.ro/mod/assign/view.php?action=grading&id=' + sys.argv[1] + '&page=', sys.argv[2],
	         sys.argv[3])
