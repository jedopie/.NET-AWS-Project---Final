using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using CloudComputingA1.Models;

namespace CloudComputingA1.Controllers;

public class MainController : Controller
{
    private readonly ILogger<MainController> _logger;

    public MainController(ILogger<MainController> logger)
    {
        _logger = logger;
        ViewBag.IsRegistered = true;
    }

    public IActionResult MainPage()
    {
        ViewBag.IsRegistered = true;
        return View();
    }

    public IActionResult Query()
    {
        ViewBag.IsRegistered = true;
        return View();
    }

    public IActionResult Subscriptions()
    {
        ViewBag.IsRegistered = true;
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}


