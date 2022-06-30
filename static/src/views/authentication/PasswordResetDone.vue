<template>
    <ProfileGeneral>
        <template #form_content="{ routes }">
            <div class="form_content">
                <div class="text-h5 q-mb-md">Password Reset</div>
                <UserAuthSnippet />
                <div class="text-body">
                    We have sent you an e-mail. If you have not received it
                    please check your spam folder. Otherwise contact us if you
                    do not receive it in a few minutes.
                </div>
            </div>
        </template>
    </ProfileGeneral>
</template>

<script setup>
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
import UserAuthSnippet from "../../components/auth/UserAuthSnippet.vue";
</script>

<style>
</style>