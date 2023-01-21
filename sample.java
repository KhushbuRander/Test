// Sample test in Java to run Automate session.

import org.openqa.selenium.By;
import org.openqa.selenium.Platform;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;

import java.net.URL;

public class JavaSample {

  public static final String AUTOMATE_USERNAME = System.getenv("BROWSERSTACK_USERNAME");
  public static final String AUTOMATE_ACCESS_KEY = System.getenv("BROWSERSTACK_ACCESS_KEY");
  public static final String LOCAL_IDENTIFIER = System.getenv("BROWSERSTACK_LOCAL_IDENTIFIER");
  public static final String BUILD_NAME = System.getenv("BROWSERSTACK_BUILD_NAME");
  public static final String PROJECT_NAME = System.getenv("BROWSERSTACK_PROJECT_NAME");

  public static final String URL = "https://" + AUTOMATE_USERNAME + ":" + AUTOMATE_ACCESS_KEY + "@hub-cloud.browserstack.com/wd/hub";

  public static void main(String[] args) throws Exception {
  DesiredCapabilities capabilities = new DesiredCapabilities();
  capabilities.setCapability("browserName", "Chrome");
  capabilities.setCapability("browserVersion", "100.0");
  HashMap<String, Object> browserstackOptions = new HashMap<String, Object>();
  browserstackOptions.put("os", "Windows");
  browserstackOptions.put("osVersion", "10");
  browserstackOptions.put("projectName", "BStack Project Name: " + PROJECT_NAME);
  browserstackOptions.put("buildName", "BStack Build Name: " + BUILD_NAME);
  browserstackOptions.put("localIdentifier", LOCAL_IDENTIFIER);
  browserstackOptions.put("seleniumVersion", "4.0.0");
  capabilities.setCapability("bstack:options", browserstackOptions);

  WebDriver driver = new RemoteWebDriver(new URL("https://" + AUTOMATE_USERNAME + ":" + AUTOMATE_ACCESS_KEY + "@hub.browserstack.com/wd/hub"), capabilities);
    driver.get("http://localhost:8099"); // HTTP Server should be running on 8099 port of GitHub runner
    System.out.println(driver.getTitle());
    driver.quit();
  }
}
