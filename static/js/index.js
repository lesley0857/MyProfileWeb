var spinner = document.getElementById("spinner")
window.addEventListener('load', () => {
    console.log('loaad');
    setTimeout(() => {
        $('.spinner').addClass("rm");
        $('.spinner').removeClass("spinner")
    }, 1500);
});