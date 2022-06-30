<template>
    <ProfileGeneral>
        <template #form_content="{ routes }">
            <!-- <div id="snippet" v-if="user_is_authenticated">
                <p v-if="user?.username">
                    <strong>Note:</strong> you are already logged in as
                    {{ user.username[0].toUpperCase()
                    }}{{ user.username.slice(1) }}.
                </p>
            </div> -->
            <UserAuthSnippet v-if="user_is_authenticated" />
            <div class="form_content q-mb-md">
                <form
                    method="POST"
                    :action="routes?.auth_routes?.account_reset_password"
                >
                    <CSRFToken />
                    <div class="q-mb-md">
                        <q-input
                            label="Email"
                            name="email"
                            v-model="formData.email"
                            type="email"
                            :error="formErrors.email !== ''"
                            :error-message="formErrors.email"
                        />
                    </div>
                    <q-btn
                        type="submit"
                        label="Reset my password"
                        color="secondary"
                        text-color="dark"
                    />
                </form>
            </div>
            <div>
                <p>
                    Please contact us if you have any trouble resetting your
                    password.
                </p>
            </div>
        </template>
    </ProfileGeneral>
</template>

<script setup>
import { inject, onBeforeMount, reactive, ref } from "@vue/runtime-core";
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
import CSRFToken from "../../components/CSRFToken.vue";
import UserAuthSnippet from "../../components/auth/UserAuthSnippet.vue";
// import getAuthUser from "../../composables/getAuthUser";

// const auth_snippet = inject("authSnippet");
const form_errors = inject("form_errors");
const old_form_data = inject("old_form_data");

const user_is_authenticated = inject("user_is_authenticated");
// const { callAuthUser } = getAuthUser();
// const user = ref({});
// onBeforeMount(async () => {
//     if (user_is_authenticated) {
//         user.value = await callAuthUser();
//     }
// });

const formData = reactive({
    email: old_form_data.email ? old_form_data.email[0].message : "",
});
console.log(form_errors);

const formErrors = reactive({
    email: form_errors.email ? form_errors.email[0].message : "",
});
</script>

<style>
</style>