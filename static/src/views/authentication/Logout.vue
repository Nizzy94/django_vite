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
import { inject } from "@vue/runtime-core";
import axios from "axios";
import { Cookies } from "quasar";

const redirect_field = inject("redirect_field");

const logout = async () => {
    const form = document.getElementById("logout_form");

    await axios.post(
        "/user/logout/",
        {},
        {
            headers: {
                "X-CSRFToken": Cookies.get("csrftoken"),
            },
            withCredentials: true,
        }
    );

    form.submit();
};
</script>

<style>
</style>