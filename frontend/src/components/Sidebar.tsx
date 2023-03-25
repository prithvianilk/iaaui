import React, { useState } from "react";

const Sidebar = () => {
  const onDragStart = (event: any, nodeType: any) => {
    event.dataTransfer.setData("application/reactflow", nodeType);
    event.dataTransfer.effectAllowed = "move";
  };

  const [clusterName, setClusterName] = useState("Cluster");

  return (
    <div>
      <div className="text-center text-lg">Create a cluster</div>
      <input type="text" />

      <div className="flex justify-center">
        <div
          className="node w-2/3 text-lg"
          onDragStart={(event) => onDragStart(event, "Cluster")}
          draggable
        >
          {clusterName}
        </div>
      </div>
      <div onDragStart={(event) => onDragStart(event, "App")} draggable>
        App
      </div>
    </div>
  );
};

export default Sidebar;
