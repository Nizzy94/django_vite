<template>
    <AuthLayout
        formTitle="Sign In"
        :submiting="logingIn"
        @sign-in="submitLogin"
        :non_field_errors="formErrors.non_field_errors"
    >
        <template #form_controls>
            <q-card-section class="q-px-lg">
                <q-input
                    label="Username/Email"
                    name="login"
                    v-model="formData.username"
                    :error="formErrors.username !== ''"
                    :error-message="formErrors.username"
                />
            </q-card-section>
            <q-card-section class="q-px-lg">
                <q-input
                    label="Password"
                    v-model="formData.password"
                    name="password"
                    :type="isPwd ? 'password' : 'text'"
                    :error="formErrors.password !== ''"
                    :error-message="formErrors.password"
                >
                    <template v-slot:append>
                        <q-icon
                            :name="isPwd ? 'visibility_off' : 'visibility'"
                            class="cursor-pointer"
                            @click="isPwd = !isPwd"
                        />
                    </template>
                </q-input>
            </q-card-section>
        </template>
    </AuthLayout>
</template>

<script setup>
import { reactive, ref } from "@vue/reactivity";
import { inject } from "@vue/runtime-core";
import AuthLayout from "./Auth.vue";
import axios from "axios";
import { Cookies } from "quasar";
import getQueries from "../../composables/getQueries";

const isPwd = ref(true);
const logingIn = ref(false);

const { getRedirectUrl } = getQueries();

const old_form_data = inject("old_form_data");
const form_errors = inject("form_errors");

console.log(old_form_data);
console.log(form_errors);

const formData = reactive({
    username: old_form_data ? old_form_data.login : "",
    password: old_form_data ? old_form_data.password : "",
});
const formErrors = reactive({
    username: form_errors.login ? form_errors.login[0].message : "",
    password: form_errors.password ? form_errors.password[0].message : "",
    non_field_errors: form_errors.non_field_errors
        ? form_errors.non_field_errors[0].message
        : "",
});

const submitLogin = async (routes) => {
    logingIn.value = true;
    console.log(formData);
    console.log(routes?.auth_routes?.rest_login);
    await axios
        .post(routes?.auth_routes?.rest_login, formData, {
            headers: {
                "X-CSRFToken": Cookies.get("csrftoken"),
            },
            withCredentials: true,
        })
        .then((res) => {
            const auth_form = document.getElementById("auth_form");
            const red_q = getRedirectUrl();
            console.log(red_q);
            window.location.replace(red_q);

            // auth_form.submit();
        })
        .catch((e) => {
            if (e.response) {
                console.log(e.response);
                let error = e.response.data;

                formErrors.username = error?.login ? error.login[0] : "";
                formErrors.password = error?.password ? error.password[0] : "";
                formErrors.non_field_errors = error?.non_field_errors
                    ? error.non_field_errors[0]
                    : "";
            } else if (e.request) {
                console.log(e.request);
            } else {
                console.log(e);
            }
        })
        .finally(() => {
            logingIn.value = false;
        });
};
</script>

<style lang="sass">
.form-card__complete-signup
    @media (min-width: $breakpoint-sm-min)
        width: 40%

    @media (min-width: $breakpoint-md-min)
        width: 400px
</style>