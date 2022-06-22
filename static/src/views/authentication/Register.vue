<template>
    <AuthLayout formTitle="Sign Up" @sign-up="submitRegister">
        <template #form_controls>
            <q-card-section class="row justify-between q-col-gutter-md">
                <div class="col-12 col-md-6">
                    <q-input
                        label="First Name"
                        v-model="formData.first_name"
                        :error="formErrors.first_name !== ''"
                        :error-message="formErrors.first_name"
                    />
                </div>
                <div class="col-12 col-md-6">
                    <q-input
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
                        v-model="formData.email"
                        :error="formData.email !== ''"
                        :error-message="formData.email"
                        type="email"
                    />
                </div>
                <div class="col-12 col-md-6">
                    <q-input
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
                        v-model="formData.password"
                        :type="isPwd ? 'password' : 'text'"
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
                        v-model="formData.password_confirm"
                        :type="isPwd ? 'password' : 'text'"
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
import AuthLayout from "./Auth.vue";

const isPwd = ref(true);

const formData = reactive({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    password: "",
    password_confirm: "",
});
const formErrors = reactive({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    password: "",
    password_confirm: "",
});

const submitRegister = () => {
    console.log(formData);
};
</script>

<style lang="sass">
.form-card__complete-signup
    @media (min-width: $breakpoint-sm-min)
        width: 60%

    @media (min-width: $breakpoint-md-min)
        width: 600px
</style>