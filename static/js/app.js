var chestnut_app = chestnut_app || {};

// Login Page
chestnut_app.login_screen = (Vue, axios, Cookies, $) => {

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
                        if (response.status >= 200) {
                            toastr.clear();
                            toastr.info(response.data.successMessage);
                        }

                        setTimeout(() => {
                            location.href = _form.attr('data-redirect-url');
                        }, 3000);
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

// Reset Password Page
chestnut_app.reset_password_screen = (Vue, axios, Cookies, $) => {

    return new Vue({
        delimiters: ['${', '}'],
        el: '#app_reset_password',
        data() {
            return {
                isInProgress: false,
            }
        },
        methods: {
            resetPasswordAction(event) {
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
                        if (response.status >= 200) {
                            toastr.clear();
                            toastr.info(response.data.successMessage);
                        }

                        setTimeout(() => {
                            location.href = _form.attr('data-redirect-url');
                        }, 3000);
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

// Install Page
chestnut_app.install_screen = (Vue, axios, Cookies, $) => {

    return new Vue({
        delimiters: ['${', '}'],
        el: '#app_install',
        data() {
            return {
                isInProgress: false,
            }
        },
        methods: {
            installAction(event) {
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
                        if (response.status >= 200) {
                            toastr.clear();
                            toastr.info(response.data.successMessage);
                        }

                        setTimeout(() => {
                            location.href = _form.attr('data-redirect-url');
                        }, 3000);
                    })
                    .catch((error) => {
                        this.isInProgress = false;
                        toastr.clear();
                        toastr.error(error.response.data.errorMessage);
                    });
            }
        }
    });

}

// Forgot Password Page
chestnut_app.forgot_password_screen = (Vue, axios, Cookies, $) => {

    return new Vue({
        delimiters: ['${', '}'],
        el: '#app_forgot_password',
        data() {
            return {
                isInProgress: false,
            }
        },
        methods: {
            forgotPasswordAction(event) {
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
                        if (response.status >= 200) {
                            toastr.clear();
                            toastr.info(response.data.successMessage);
                        }

                        setTimeout(() => {
                            location.href = _form.attr('data-redirect-url');
                        }, 3000);
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

// Settings Page
chestnut_app.settings_screen = (Vue, axios, Cookies, $) => {

    return new Vue({
        delimiters: ['${', '}'],
        el: '#app_settings',
        data() {
            return {
                isInProgress: false,
            }
        },
        methods: {
            settingsAction(event) {
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
                        if (response.status >= 200) {
                            toastr.clear();
                            toastr.info(response.data.successMessage);
                        }
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

// Profile Page
chestnut_app.profile_screen = (Vue, axios, Cookies, $) => {

    return new Vue({
        delimiters: ['${', '}'],
        el: '#app_profile',
        data() {
            return {
                isInProgress: false,
            }
        },
        methods: {
            profileAction(event) {
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
                        if (response.status >= 200) {
                            toastr.clear();
                            toastr.info(response.data.successMessage);
                        }
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
        chestnut_app.login_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_reset_password")) {
        chestnut_app.reset_password_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_install")) {
        chestnut_app.install_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_forgot_password")) {
        chestnut_app.forgot_password_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_settings")) {
        chestnut_app.settings_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_profile")) {
        chestnut_app.profile_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }
});
