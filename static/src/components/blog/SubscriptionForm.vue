<template>
    <!-- <div class="text-body1">Send us a message below.</div> -->
    <div class="" style="">
        <q-input
            v-model="subscriptionFormData.name"
            hint="Enter full name"
            hide-hint
            label="Name"
        />
    </div>
    <div class="">
        <q-input
            v-model="subscriptionFormData.email"
            type="email"
            hint="Enter email address"
            hide-hint
            label="Email"
        />
    </div>
    <div class="flex justify-center">
        <q-btn label="Subscribe" color="secondary" text-color="dark" />
    </div>
</template>

<script setup>
import { reactive } from "@vue/reactivity";

const subscriptionFormData = reactive({
    name: "",
    email: "",
});
</script>

<style>
</style>