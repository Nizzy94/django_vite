<template>
    <AuthLayout formTitle="Sign In" @sign-in="submitLogin">
        <template #form_controls>
            <q-card-section class="q-px-lg">
                <q-input
                    label="Username/Email"
                    name="login"
                    v-model="formData.login"
                    :error="formErrors.login !== ''"
                    :error-message="formErrors.login"
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

const isPwd = ref(true);

const old_form_data = inject("old_form_data");
const form_errors = inject("form_errors");

console.log(old_form_data);
console.log(form_errors);

const formData = reactive({
    login: old_form_data.login,
    password: old_form_data.password,
});
const formErrors = reactive({
    login: form_errors.login ? form_errors.login[0].message : "",
    password: form_errors.password ? form_errors.password[0].message : "",
});

const submitLogin = () => {
    console.log(formData);
};
</script>

<style lang="sass">
.form-card__complete-signup
    @media (min-width: $breakpoint-sm-min)
        width: 40%

    @media (min-width: $breakpoint-md-min)
        width: 400px
</style>