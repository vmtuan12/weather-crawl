LIST_MONTH_OF_YEAR = "//body//*[@id='Sidebar-ContainerCell']//div[@class='Sidebar-section Sidebar-month_section']//a"
LIST_DAY_OF_MONTH = "//body//*[@id='Sidebar-ContainerCell']//div[@class='Sidebar-section Sidebar-day_section']/span[not(contains(@class, 'Sidebar-nav_faded'))]/a"

DAY_TIME_HEADER = "//body//*[@id='Report-Content']//*[@id='History-MetarReports-TableHeader']/parent::*/tbody/tr[@id]/child::td"
DAY_TIME_VALUE = "//body//*[@id='Report-Content']//*[@id='History-MetarReports-TableHeader']/parent::*/tbody/tr[@id]/child::td[1]"
DAY_TIME_TEMPERATURE = "//body//*[@id='Report-Content']//*[@id='History-MetarReports-TableHeader']/parent::*/tbody/tr[@id]/child::td[2]"
DAY_TIME_WIND = "//body//*[@id='Report-Content']//*[@id='History-MetarReports-TableHeader']/parent::*/tbody/tr[@id]/child::td[4]"

TIME_WEATHER = "//body//*[@id='Report-Content']//*[@id='History-MetarReports-TableHeader']/parent::*/tbody/tr[not(@id)]//td[starts-with(text(), 'Thời Tiết')]/following-sibling::td"
