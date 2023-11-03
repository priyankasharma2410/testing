import org.openqa.selenium.By;

import org.openqa.selenium.WebDriver;

import org.openqa.selenium.chrome.ChromeDriver;

import org.openqa.selenium.support.ui.ExpectedConditions;

import org.openqa.selenium.support.ui.WebDriverWait;

public class Homepage {

public static void main(String[] args) {

System.setProperty("webdriver.chrome.driver","");

WebDriver driver = new ChromeDriver();

String baseUrl = "”Domino’s Pizza – Order Online | Get 2 Regular Pizza @99 Each (dominos.co.in);

driver.get(baseUrl);

driver.findElement(By.xpath("////body/div[@id='ymPluginDivContainerInitial']/div[@id='ymDivCircle']/img[1]")).click();

WebDriverWait wait = new WebDriverWait(driver,60) ;

wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//strong[contains(text(),'Stores near me')]")));

driver.findElement(By.xpath("//strong[contains(text(),'Stores near me')]")).click();

System.out.println("Found the button, clicked on that...");

driver.close();

System.exit(0);

}

}
