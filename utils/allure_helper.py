import os
import subprocess
import json
import platform
import sys
import shutil
from config.settings import Config
import allure

class AllureHelper:

    #setup allure report including env, executor, copy history, and attach ss
    @staticmethod
    def create_environment(results_dir):
        os.makedirs(results_dir, exist_ok=True)

        environment = {
            "Project": Config.BASE_URL,
            "Environment": Config.ENVIRONMENT,
            "Browser": Config.BROWSER,
            "Headless": Config.HEADLESS,
            "OS": platform.platform(),
            "Python": sys.version.split()[0],
        }
        file_path = os.path.join(
            results_dir,
            "environment.properties"
        )
        with open(file_path, "w", encoding="utf-8") as file:
            for key, value in environment.items():
                file.write(f"{key}={value}\n")

    @staticmethod
    def create_executor(results_dir):
        os.makedirs(results_dir, exist_ok=True)

        executor = {
            "name": "Local - Maolana Hadiar",
            "type": "Local",
            "buildName": "Manual Execution",
            "buildOrder": 1,
        }
        file_path = os.path.join(
            results_dir,
            "executor.json"
        )
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(executor, file, indent=4)
            
    @staticmethod
    def copy_history(results_dir, report_dir):
        source = os.path.join(report_dir, "history")
        destination = os.path.join(results_dir, "history")

        if os.path.exists(source):
            shutil.copytree(
                source,
                destination,
                dirs_exist_ok=True
            )
    
    @staticmethod
    def attach_screenshot(driver, name="TEST_FAILED_SCREENSHOT"):
        allure.attach(
            driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    #setup allure to generate report and make it auto open after running test
    @staticmethod
    def generate_report(results_dir, report_dir):
        subprocess.run(
            [
                "allure",
                "generate",
                results_dir,
                "-o",
                report_dir,
                "--clean",
            ],
            check=True,
        )

    @staticmethod
    def open_report(report_dir):
        subprocess.run(
            [
                "allure",
                "open",
                report_dir,
            ],
            check=True,
        )
    
    #setup allure categories to catch some errors
    @staticmethod
    def create_categories(results_dir):
        os.makedirs(results_dir, exist_ok=True)
        
        categories = [
            {
                "name": "Assertion Failure",
                "matchedStatuses": ["failed"],
                "traceRegex": ".*AssertionError.*"
            },
            {
                "name": "Element Not Found",
                "matchedStatuses": ["failed"],
                "traceRegex": ".*NoSuchElementException*."
            },
            {
                "name": "Timeout",
                "matchedStatuses": ["failed"],
                "traceRegex": ".*TimeoutException*."
            },
            {
                "name": "Element Not Clickable",
                "matchedStatuses": ["failed"],
                "traceRegex": ".*ElementClickInterceptedException*."
            },
            {
                "name": "Locator Broken",
                "matchedStatuses": ["failed"],
                "traceRegex": ".*StaleElementReferenceException*."
            }
        ]
        with open(
            os.path.join(results_dir, "categories.json"),
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(categories, f, indent=4)