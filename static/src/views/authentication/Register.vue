<template>
    <AuthLayout formTitle="Sign Up" @sign-up="submitRegister">
        <template #form_controls>
            <q-card-section class="row justify-between q-col-gutter-md">
                <div class="col-12 col-md-6">
                    <q-input
                        name="first_name"
                        label="First Name"
                        v-model="formData.first_name"
                        :error="formErrors.first_name !== ''"
                        :error-message="formErrors.first_name"
                    />
                </div>
                <div class="col-12 col-md-6">
                    <q-input
                        name="last_name"
                        label="Last Name"
                        v-model="formData.last_name"
                        :error="formErrors.last_name !== ''"
                        :error-message="formErrors.last_name"
                    />
                </div>
            </q-card-section>

            <q-card-section class="row justify-between q-col-gutter-md">
                <div class="col-12 col-md-6">
                    <q-input
                        label="Email"
                        name="email"
                        v-model="formData.email"
                        :error="formErrors.email !== ''"
                        :error-message="formErrors.email"
                        type="email"
                    />
                </div>
                <div class="col-12 col-md-6">
                    <q-input
                        name="username"
                        label="Username"
                        v-model="formData.username"
                        :error="formErrors.username !== ''"
                        :error-message="formErrors.username"
                    />
                </div>
            </q-card-section>

            <q-card-section class="row justify-between q-col-gutter-md">
                <div class="col-12 col-md-6">
                    <q-input
                        label="Password"
                        name="password1"
                        v-model="formData.password1"
                        :type="isPwd ? 'password' : 'text'"
                        :error="formErrors.password1 !== ''"
                        :error-message="formErrors.password1"
                    >
                        <template v-slot:append>
                            <q-icon
                                :name="isPwd ? 'visibility_off' : 'visibility'"
                                class="cursor-pointer"
                                @click="isPwd = !isPwd"
                            />
                        </template>
                    </q-input>
                </div>
                <div class="col-12 col-md-6">
                    <q-input
                        label="Confirm Password"
                        name="password2"
                        v-model="formData.password2"
                        :type="isPwd ? 'password' : 'text'"
                        :error="formErrors.password2 !== ''"
                        :error-message="formErrors.password2"
                    >
                        <template v-slot:append>
                            <q-icon
                                :name="isPwd ? 'visibility_off' : 'visibility'"
                                class="cursor-pointer"
                                @click="isPwd = !isPwd"
                            />
                        </template>
                    </q-input>
                </div>
            </q-card-section>
        </template>
    </AuthLayout>
</template>

<script setup>
import { reactive, ref } from "@vue/reactivity";
import { inject } from "@vue/runtime-core";
import AuthLayout from "./Auth.vue";

const isPwd = ref(true);

// console.log(inject("form_errors").last_name[0].message);
const old_form_data = inject("old_form_data");
const form_errors = inject("form_errors");

const formData = reactive({
    first_name: old_form_data.first_name,
    last_name: old_form_data.last_name,
    username: old_form_data.username,
    email: old_form_data.email,
    password1: old_form_data.password1,
    password2: old_form_data.password2,
});
const formErrors = reactive({
    first_name: form_errors.first_name ? form_errors.first_name[0].message : "",
    last_name: form_errors.last_name ? form_errors.last_name[0].message : "",
    username: form_errors.username ? form_errors.username[0].message : "",
    email: form_errors.email ? form_errors.email[0].message : "",
    password1: form_errors.password1 ? form_errors.password1[0].message : "",
    password2: form_errors.password2 ? form_errors.password2[0].message : "",
});

const submitRegister = () => {
    const form = document.getElementById("auth_form");
    console.log(formData);
    form.submit();
};
</script>

<style lang="sass">
.form-card__complete-signup
    @media (min-width: $breakpoint-sm-min)
        width: 60%

    @media (min-width: $breakpoint-md-min)
        width: 600px
</style>