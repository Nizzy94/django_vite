<template>
    <ProfileGeneral>
        <template #form_content>
            <div class="form_content">
                <div class="text-h6 q-mb-md">
                    {{
                        messages.length
                            ? messages[0].message
                            : "Check your email for verification link"
                    }}
                </div>
                <p>
                    We have sent an e-mail to you for verification. Follow the
                    link provided to finalize the signup process. If you do not
                    see the verification e-mail in your main inbox, check your
                    spam folder. Please contact us if you do not receive the
                    verification e-mail within a few minutes.
                </p>
            </div>
        </template>
    </ProfileGeneral>
</template>

<script setup>
import { inject } from "@vue/runtime-core";
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
const messages = inject("messages");
</script>

<style lang="sass">
// .form_content
//     width: 100%
//     @media (min-width: $breakpoint-md-min)
//         width: 70%
//     @media (min-width: $breakpoint-lg-min)
//         width: 50%
</style>