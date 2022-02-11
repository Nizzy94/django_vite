<template>
    <div class="column side_bar">
        <div class="bg-grey-4" style="height: 200px"></div>
        <div class="text-h6 q-mt-xl text-primary">Subscribe for update</div>
        <subscription-form />
    </div>
</template>

<script setup>
import SubscriptionForm from "./SubscriptionForm.vue";
</script>

<style lang="sass">
.side_bar
    position: sticky
    top: 15px
</style>