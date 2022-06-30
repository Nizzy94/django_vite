<template>
    <ProfileGeneral>
        <template #form_content="{ routes }">
            <div class="text-h5 q-mb-md">Set Password</div>

            <div class="form_content">
                <form
                    method="POST"
                    :action="routes?.auth_routes?.account_set_password"
                    class=""
                >
                    <!-- <div v-if="message" class="q-mb-md"> -->
                    <div
                        class=""
                        v-if="messages.length"
                        v-for="(message, i) in messages"
                        :key="i"
                    >
                        <span
                            :class="{
                                'text-negative': message.tag == 'error',
                                'text-positive': message.tag == 'success',
                                'text-info': message.tag == 'info',
                                'text-warning': message.tag == 'warning',
                            }"
                        >
                            {{ message.message }}
                        </span>
                    </div>
                    <!-- </div> -->
                    <div v-if="formErrors.non_field_errors" class="q-mb-md">
                        <div
                            v-for="error in formErrors.non_field_errors"
                            :key="error"
                            class="text-negative"
                        >
                            {{ error.message }}
                        </div>
                    </div>
                    <CSRFToken />

                    <div class="q-mb-md">
                        <q-input
                            name="password1"
                            v-model="formData.password1"
                            label="New Password"
                            :error="formErrors.password1 != ''"
                            :error-message="formErrors.password1"
                        />
                    </div>
                    <div class="q-mb-md">
                        <q-input
                            name="password2"
                            v-model="formData.password2"
                            label="Confirm New Password"
                            :error="formErrors.password2 != ''"
                            :error-message="formErrors.password2"
                        />
                    </div>
                    <div>
                        <q-btn
                            label="Set Password"
                            type="submit"
                            name="action"
                            color="secondary"
                            class="q-mb-md"
                            text-color="dark"
                        />
                    </div>
                </form>
            </div>
        </template>
    </ProfileGeneral>
</template>

<script setup>
import { inject, reactive } from "@vue/runtime-core";
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
import CSRFToken from "../../components/CSRFToken.vue";

// const token_fail = inject("token_fail");
const old_form_data = inject("old_form_data");
const form_errors = inject("form_errors");
const messages = inject("messages");
// const action_url = inject("action_url");

// console.log(token_fail);

const formData = reactive({
    // oldpassword: old_form_data ? old_form_data.oldpassword : "",
    password1: old_form_data ? old_form_data.password1 : "",
    password2: old_form_data ? old_form_data.password2 : "",
});
const formErrors = reactive({
    // oldpassword: form_errors.oldpassword
    //     ? form_errors.oldpassword[0].message
    //     : "",
    password1: form_errors.password1 ? form_errors.password1[0].message : "",
    password2: form_errors.password2 ? form_errors.password2[0].message : "",
    non_field_errors: form_errors.non_field_errors
        ? form_errors.non_field_errors
        : "",
});
</script>

<style>
</style>