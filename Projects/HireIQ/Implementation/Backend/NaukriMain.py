
from NaukriFunctions import *

def main():
    driver = getDriver(verbose=True)
    # autoLogin(driver)
    openJobsPage(driver=driver, verbose=True)
    sortJobs(driver=driver, verbose=True)
    # 
    job_links = getJobLinks(driver=driver, verbose=True)
    print(job_links)
    # 
    if not job_links:
        print("No jobs found")
        return
    # 
    # Scrape first job (for testing)
    job_data = scrapeJobDetail(driver=driver, url=job_links[0], verbose=True)
    print("\nSCRAPED JOB DATA:")
    for k, v in job_data.items():
        print(f"{k}: {v}")
    # 
    input("\nPress ENTER to close browser")
    driver.quit()


if __name__ == "__main__":
    main()
