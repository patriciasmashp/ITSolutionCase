const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('success')) {
    const toastLiveExample = document.getElementById('liveToast')


    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    toastLiveExample.querySelector("#toast-body").innerHTML = `запись ${urlParams.get('success')} успешно создана`
    toastBootstrap.show()

}
