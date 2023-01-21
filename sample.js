var webdriver = require('selenium-webdriver');

// Input capabilities
var capabilities = {
  'bstack:options' : {
    "os" : "Windows",
    "osVersion" : "10",
    "projectName" : "BStack Project Name: " + projectName,
    "buildName" : "BStack Build Name: " + buildName,
    "localIdentifier" : localIdentifier,
    "userName" : username,
    "accessKey" : accessKey,
    "seleniumVersion" : "4.0.0",
  },
    "browserName" : "Chrome",
    "browserVersion" : "100.0",
}

var driver = new webdriver.Builder().
  usingServer("https://hub-cloud.browserstack.com/wd/hub").
  withCapabilities(capabilities).
  build();

// HTTP Server should be running on 8099 port of GitHub runner
driver.get('http://localhost:8099').then(function () {
  driver.getTitle().then(function (title) {
    console.log(title);
    driver.quit();
  });
});
