const urls = {
    deletePayment: "/delete",
    createPayment: "",
    updatePayment: "",
    sendForm: "/sendForm",
    getPayment: "/getPayment",
    filter: "/filter"
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

class LinkedList {
    constructor(name, value) {
        this.value = value;
        this.name = name
        this.next = null;

    }

    append(name, value) {
        // Создаём новый узел.

        // Если нет head или tail, делаем новым узлом head и tail.
        if (!this.next) {
            this.next = new LinkedList(name, value);

            return this;
        }
        else {
            this.next.append(name, value);
        }

        return this;
    }
    findByName(name) {
        if (this.name === name) {
            return this;
        }
        else {
            if (this.next !== null) {

                return this.next.findByName(name);
            }
            return null;
        }
    }

    getTail() {
        if (!this.next) {
            return this;
        }
        else {
            this.next.getTail();
        }
    }
    foreach(callback) {
        callback(this);
        if (this.next) {
            this.next.foreach(callback);
        }
    }
    toObj() {
        let obj = {};
        this.foreach((node) => {
            obj[node.name] = node.value;
        });
        return obj;
    }
}

class Filter {
    constructor() {
        this.timeStart = null;
        this.timeEnd = null;
        this.statusId = null;
        this.typeId = null;
        this.categoryId = null;
        this.subcategoryId = null;
    }
    async filter() {
        let responce = await axios.post(urls.filter, this, {
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
        })
        return responce.data.payments
    }
}