import React, { useState } from "react";

export type NodeMeta = {
  nodeType: "input" | "output";
  label: string;
};

const Sidebar = () => {
  const onDragStart = (event: any, data: NodeMeta) => {
    event.dataTransfer.setData("label", data.label);
    event.dataTransfer.setData("type", data.nodeType);
    event.dataTransfer.effectAllowed = "move";
  };

  const [clusterName, setClusterName] = useState("Cluster");

  return (
    <div>
      <div className="text-center text-lg">Create a cluster</div>
      <div className="flex flex-col justify-center">
        <input
          type="text"
          placeholder="Enter cluster name"
          onChange={(e) => setClusterName(e.currentTarget.value)}
        />
        <div
          className="node w-2/3 text-lg"
          onDragStart={(event) =>
            onDragStart(event, { label: clusterName, nodeType: "input" })
          }
          draggable
        >
          {clusterName}
        </div>
      </div>
      <div
        className="node w-2/3 text-lg"
        onDragStart={(event) =>
          onDragStart(event, { label: "App", nodeType: "output" })
        }
        draggable
      >
        App
      </div>
    </div>
  );
};

export default Sidebar;
