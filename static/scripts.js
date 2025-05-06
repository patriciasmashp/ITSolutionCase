


const deletePayment = (id) => {

    axios.delete(urls.deletePayment + "/" + id, {
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // Установка CSRF-токена в заголовок
        },
    }).then((responce) => {
        if (responce.data.success) {
            document.querySelector(`tr[data-payment="${id}"]`).remove()
        }

    })
}

const getPayment = (id) => {
    axios.get(urls.getPayment + "/" + id, {
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // Установка CSRF-токена в заголовок
        },
    }).then((responce) => {
        if (responce.data) {
            console.log(document.getElementById('editPaymentForm'));
            document.getElementById('editPaymentForm').innerHTML = responce.data
        }

    })
}

const addPayment = new bootstrap.Modal('#createPaymentModal')
const toogleModalPayment = () => {

    addPayment.toggle()
}

const editPaymentModal = new bootstrap.Modal('#editPaymentModal')

const toogleModalEditPayment = (id) => {
    getPayment(id)
    document.querySelector('#errorEditPayment').innerHTML = ""

    editPaymentModal.toggle()
}

const editPayment = () => {
    const form = document.getElementById('editPaymentForm')
    const id = form.querySelector('input[name="id"]').value
    console.log(document.querySelector('#errorEditPayment'));


    axios.post(urls.updatePayment + "/" + id, form, {
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
    }).then((response) => {
        const tableBody = document.getElementById('paymentsTableBody')
        tableBody.querySelector(`tr[data-payment="${id}"]`).innerHTML = response.data
        editPaymentModal.toggle()
    }).catch((error) => {

        if (error.status === 400) {
            document.querySelector('#errorEditPayment').innerHTML = error.response.data
        }
    })
}

const addPaymentForm = document.getElementById("addPaymentForm")

if (addPaymentForm) {
    // Добавление платежа работает с помощью связанного списка.
    // При изменении родительского узла, меняется весь хвост
    const submitButton = document.getElementById('submitPaymentAddForm')
    let linkedList = new LinkedList("payment_type", undefined)

    const sendPaymendAddForm = () => {
        linkedList.append('filled', true)

        axios.post(urls.createPayment, linkedList.toObj(), {
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
        }).then((response) => {
            const tableBody = document.getElementById('paymentsTableBody')
            tableBody.innerHTML = tableBody.innerHTML + response.data
            linkedList.next.foreach((node) => {
                if (node.next !== null && node.name != "filled")

                    addPaymentForm.querySelector(`[name="${node.name}"]`).remove()
            })
            addPaymentForm.querySelector(`[name="payment_type"]`).value = ""
            linkedList = new LinkedList("payment_type", undefined)
            toogleModalPayment()
        })
    }

    submitButton.addEventListener('click', sendPaymendAddForm)


    addPaymentForm.addEventListener('change', (e) => {
        e.preventDefault()
        let chnaged = linkedList.findByName(e.target.name)
        if (chnaged.name == "comment") {
            chnaged.value = e.target.value
            return
        }
        chnaged.value = e.target.value

        if (chnaged.next != null) {
            console.log(linkedList);

            chnaged.foreach((node) => {
                if (node.next !== null)

                    addPaymentForm.querySelector(`[name="${node.next.name}"]`).remove()
            })

            chnaged.next = null
            submitButton.setAttribute('disabled', true)
        }
        if (chnaged.value == "") {
            return
        }

        axios.post(urls.sendForm, linkedList, {
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
        }).then((response) => {
            console.log(response.data.status);

            if (response.data.filled) {
                submitButton.removeAttribute('disabled')

                console.log(addPaymentForm.querySelector(`[name="comment"]`));

                if (!addPaymentForm.querySelector(`[name="comment"]`)) {
                    const container = document.createElement('div')
                    container.innerHTML = response.data.comment
                    addPaymentForm.appendChild(container)
                    linkedList.append('comment', undefined)

                }

                return
            }
            const container = document.createElement('div')
            container.innerHTML = response.data
            addPaymentForm.appendChild(container)
            linkedList.append(container.firstChild.name, undefined)
        })

    })

}