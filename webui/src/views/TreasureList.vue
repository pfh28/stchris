<template>
  <main>
  <div name="listContainer" class="w-full h-full space-y-2">
    <TreasureItem v-for="treasure in treasureList" :key="treasure.id" 
        :treasure="treasure"/>
  </div>
  </main>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import {useTreasureStore} from '../stores/treasureStore'
import TreasureItem from '../components/TreasureItem.vue';

const treasureStore = useTreasureStore();

const {treasureList} = storeToRefs(treasureStore)

console.log(treasureList);

treasureStore.getTreasureList();

</script>