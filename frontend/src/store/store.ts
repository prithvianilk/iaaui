import create from "zustand";

const useStore = create((set) => ({
  color: "white",
}));

export default useStore;
