var rabbit_app = rabbit_app || {};

// Login Page
rabbit_app.login_screen = (Vue, axios, Cookies, $) => {

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
rabbit_app.reset_password_screen = (Vue, axios, Cookies, $) => {

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
rabbit_app.install_screen = (Vue, axios, Cookies, $) => {

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
rabbit_app.forgot_password_screen = (Vue, axios, Cookies, $) => {

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
rabbit_app.settings_screen = (Vue, axios, Cookies, $) => {

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
rabbit_app.profile_screen = (Vue, axios, Cookies, $) => {

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
            },

            accessAction(event) {
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
                            window.location.reload();
                        }, 30);
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

// Create Host Group Page
rabbit_app.create_group_screen = (Vue, axios, Cookies, $) => {

    return new Vue({
        delimiters: ['${', '}'],
        el: '#app_group_create',
        data() {
            return {
                isInProgress: false,
            }
        },
        methods: {
            createGroupAction(event) {
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
                            toastr.info(_i18n.resource_created);
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

// Update Host Group Page
rabbit_app.update_group_screen = (Vue, axios, Cookies, $) => {

    return new Vue({
        delimiters: ['${', '}'],
        el: '#app_group_update',
        data() {
            return {
                isInProgress: false,
            }
        },
        methods: {
            updateGroupAction(event) {
                event.preventDefault();
                this.isInProgress = true;

                let inputs = {};
                let _self = $(event.target);
                let _form = _self.closest("form");

                _form.serializeArray().map((item, index) => {
                    inputs[item.name] = item.value;
                });

                axios.put(_form.attr('action'), inputs)
                    .then((response) => {
                        if (response.status >= 200) {
                            toastr.clear();
                            toastr.info(_i18n.resource_updated);
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


// Group List Page
rabbit_app.group_list_screen = (Vue, axios, Cookies, $) => {

    return new Vue({
        delimiters: ['${', '}'],
        el: '#app_group_list',
        data() {
            return {
                offset: 0,
                showLoad: false,
                groups: [

                ],
                noRecords: false,
            }
        },
        methods: {
            getNextHostGroups(event) {
                axios.get(app_globals.group_list_url + "?offset=" + this.offset)
                    .then((response) => {
                        var result = [];

                        for (let i = 0; i < response.data.groups.length; i++) {

                            response.data.groups[i]["editLink"] = app_globals.group_edit_url.replace(
                                "__",
                                response.data.groups[i].id
                            );

                            response.data.groups[i]["deleteLink"] = app_globals.group_delete_endpoint.replace(
                                "__",
                                response.data.groups[i].id
                            );

                            result.push(response.data.groups[i]);
                        }

                        this.groups = this.groups.concat(result);
                        this.offset += 20;

                        if (this.offset >= response.data._metadata.totalCount) {
                            this.showLoad = false;
                        } else {
                            this.showLoad = true;
                        }
                    })
                    .catch((error) => {
                        toastr.clear();
                        toastr.error(error.response.data.errorMessage);
                    });
            },

            deleteGroup(event) {
                event.preventDefault();

                let _self = $(event.target);

                if (window.confirm("Are you sure?")) {
                    axios.delete(_self.attr("endpoint"))
                        .then((response) => {
                            if (response.status >= 200) {
                                toastr.clear();
                                toastr.info(_i18n.resource_deleted);
                            }

                            setTimeout(() => {
                                location.reload();
                            }, 3000);
                        })
                        .catch((error) => {
                            toastr.clear();
                            toastr.error(error.response.data.errorMessage);
                        });
                }
            }
        },
        mounted() {
            axios.get(app_globals.group_list_url + "?offset=" + this.offset)
                .then((response) => {
                    var result = [];

                    for (let i = 0; i < response.data.groups.length; i++) {

                        response.data.groups[i]["editLink"] = app_globals.group_edit_url.replace(
                            "__",
                            response.data.groups[i].id
                        );

                        response.data.groups[i]["deleteLink"] = app_globals.group_delete_endpoint.replace(
                            "__",
                            response.data.groups[i].id
                        );

                        result.push(response.data.groups[i]);
                    }

                    this.groups = this.groups.concat(result);
                    this.offset += 20;

                    if (response.data._metadata.totalCount == 0) {
                        this.noRecords = true;
                    }

                    if (this.offset >= response.data._metadata.totalCount) {
                        this.showLoad = false;
                    } else {
                        this.showLoad = true;
                    }
                })
                .catch((error) => {
                    toastr.clear();
                    toastr.error(error.response.data.errorMessage);
                });
        }
    });

}

// Create Key Page
rabbit_app.create_key_screen = (Vue, axios, Cookies, $) => {

    return new Vue({
        delimiters: ['${', '}'],
        el: '#app_key_create',
        data() {
            return {
                isInProgress: false,
            }
        },
        methods: {
            createKeyAction(event) {
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
                            toastr.info(_i18n.resource_created);
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
            },

            generateKeys(event) {
                event.preventDefault();

                axios.get(app_globals.generate_keys, {})
                    .then((response) => {
                        if (response.status >= 200) {
                            $('[name="publicKey"]').val(response.data.publicKey);
                            $('[name="privateKey"]').val(response.data.privateKey);
                        }
                    })
                    .catch((error) => {
                        // Show error
                        toastr.clear();
                        toastr.error(error.response.data.errorMessage);
                    });
            }
        }
    });

}

// Key List Page
rabbit_app.key_list_screen = (Vue, axios, Cookies, $) => {

    return new Vue({
        delimiters: ['${', '}'],
        el: '#app_key_list',
        data() {
            return {
                offset: 0,
                showLoad: false,
                keys: [

                ],
                noRecords: false,
            }
        },
        methods: {
            getNextKeys(event) {
                axios.get(app_globals.key_list_url + "?offset=" + this.offset)
                    .then((response) => {
                        var result = [];

                        for (let i = 0; i < response.data.keys.length; i++) {
                            response.data.keys[i]["deleteLink"] = app_globals.key_delete_endpoint.replace(
                                "__",
                                response.data.keys[i].id
                            );

                            result.push(response.data.keys[i]);
                        }

                        this.keys = this.keys.concat(result);
                        this.offset += 20;

                        if (this.offset >= response.data._metadata.totalCount) {
                            this.showLoad = false;
                        } else {
                            this.showLoad = true;
                        }
                    })
                    .catch((error) => {
                        toastr.clear();
                        toastr.error(error.response.data.errorMessage);
                    });
            },

            deleteKey(event) {
                event.preventDefault();

                let _self = $(event.target);

                if (window.confirm("Are you sure?")) {
                    axios.delete(_self.attr("endpoint"))
                        .then((response) => {
                            if (response.status >= 200) {
                                toastr.clear();
                                toastr.info(_i18n.resource_deleted);
                            }

                            setTimeout(() => {
                                location.reload();
                            }, 3000);
                        })
                        .catch((error) => {
                            toastr.clear();
                            toastr.error(error.response.data.errorMessage);
                        });
                }
            }
        },
        mounted() {
            axios.get(app_globals.key_list_url + "?offset=" + this.offset)
                .then((response) => {
                    var result = [];

                    for (let i = 0; i < response.data.keys.length; i++) {
                        response.data.keys[i]["deleteLink"] = app_globals.key_delete_endpoint.replace(
                            "__",
                            response.data.keys[i].id
                        );

                        result.push(response.data.keys[i]);
                    }

                    this.keys = this.keys.concat(result);
                    this.offset += 20;

                    if (response.data._metadata.totalCount == 0) {
                        this.noRecords = true;
                    }

                    if (this.offset >= response.data._metadata.totalCount) {
                        this.showLoad = false;
                    } else {
                        this.showLoad = true;
                    }
                })
                .catch((error) => {
                    toastr.clear();
                    toastr.error(error.response.data.errorMessage);
                });
        }
    });

}

$(document).ready(() => {
    axios.defaults.headers.common = {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': Cookies.get('csrftoken')
    };

    if (document.getElementById("app_login")) {
        rabbit_app.login_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_reset_password")) {
        rabbit_app.reset_password_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_install")) {
        rabbit_app.install_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_forgot_password")) {
        rabbit_app.forgot_password_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_settings")) {
        rabbit_app.settings_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_profile")) {
        rabbit_app.profile_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_group_create")) {
        rabbit_app.create_group_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_group_update")) {
        rabbit_app.update_group_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_group_list")) {
        rabbit_app.group_list_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_key_create")) {
        rabbit_app.create_key_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }

    if (document.getElementById("app_key_list")) {
        rabbit_app.key_list_screen(
            Vue,
            axios,
            Cookies,
            $
        );
    }
});
