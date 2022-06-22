<template>
    <AuthLayout formTitle="Sign In" @sign-in="submitLogin">
        <template #form_controls>
            <q-card-section class="q-px-lg">
                <q-input label="Username/Email" v-model="formData.login" />
            </q-card-section>
            <q-card-section class="q-px-lg">
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
            </q-card-section>
        </template>
    </AuthLayout>
</template>

<script setup>
import { reactive, ref } from "@vue/reactivity";
import AuthLayout from "./Auth.vue";

const isPwd = ref(true);

const formData = reactive({
    login: "",
    password: "",
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