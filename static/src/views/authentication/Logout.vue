<template>
    <ProfileGeneral>
        <template #form_content="{ routes }">
            <p class="q-mb-md">Are you sure you want to sign out?</p>
            <form
                method="post"
                :action="routes?.auth_routes?.account_logout"
                id="logout_form"
            >
                <CSRFToken />

                <input
                    type="hidden"
                    v-if="redirect_field.value != 'None'"
                    :name="redirect_field.name"
                    :value="redirect_field.value"
                />

                <q-btn
                    label="Sign Out"
                    color="negative"
                    :loading="logingOut"
                    type="submit"
                    @click.prevent="logout"
                />
            </form>
        </template>
    </ProfileGeneral>
</template>

<script setup>
import CSRFToken from "../../components/CSRFToken.vue";
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
import { inject, ref } from "@vue/runtime-core";
import axios from "axios";
import { Cookies } from "quasar";

const redirect_field = inject("redirect_field");
const logingOut = ref(false);

const logout = async () => {
    logingOut.value = true;
    const form = document.getElementById("logout_form");

    await axios
        .post(
            "/user/logout/",
            {},
            {
                headers: {
                    "X-CSRFToken": Cookies.get("csrftoken"),
                },
                withCredentials: true,
            }
        )
        .then((res) => {})
        .catch((e) => {
            consoel.log(e);
        })
        .finally(() => {
            logingOut.value = false;
        });

    form.submit();
};
</script>

<style>
</style>