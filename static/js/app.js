
var hustle_app = hustle_app || {};

hustle_app.login_screen = (Vue, axios, Cookies, $) => {

    return new Vue({
        delimiters: ['${', '}'],
        el: '#app_login',
        data() {
            return {
                isInProgress: false,
            }
        },
        methods: {
            loginAction(event) {
                event.preventDefault();
                this.isInProgress = true;

                let inputs = {};
                let _self = $(event.target);
                let _form = _self.closest("form");

                _form.serializeArray().map((item, index) => {
                    inputs[item.name] = item.value;
                });

				axios.post(_form.attr('action'), inputs)
				  	.then((response) => {
                        // Redirect or refresh the page
				    	console.log(response.status);
				    	this.isInProgress = false;
				  	})
				  	.catch((error) => {
				  		this.isInProgress = false;
                        // Show error
                        toastr.clear();
				    	toastr.error(error.response.data.errorMessage);
				  	});
            }
        }
    });

}

$(document).ready(() => {
    axios.defaults.headers.common = {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': Cookies.get('csrftoken')
    };

    if (document.getElementById("app_login")) {
        hustle_app.login_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }
});
