import { useState } from "react";

export type NodeMeta = {
  nodeType: "input" | "output";
  label: string;
};

type SidebarProps = {
  submit: () => void;
};

const Sidebar = ({ submit }: SidebarProps) => {
  const onDragStart = (event: any, data: NodeMeta) => {
    event.dataTransfer.setData("label", data.label);
    event.dataTransfer.setData("type", data.nodeType);
    const isCluster = data.nodeType === "input";
    if (isCluster) {
      event.dataTransfer.setData("numberOfHosts", numberOfHosts.toString());
    }
    event.dataTransfer.effectAllowed = "move";
  };

  const [clusterName, setClusterName] = useState("Cluster");
  const [numberOfHosts, setNumberOfHosts] = useState(1);

  const getClusterNameWithDefaults = () => {
    return clusterName.length ? clusterName : "Cluster";
  };

  return (
    <div className="px-2">
      <div className="text-center text-lg">Create a cluster</div>
      <div className="flex flex-col justify-center">
        <label>Cluster Name</label>
        <input
          value={clusterName}
          type="text"
          placeholder="Cluster"
          onChange={(e) => setClusterName(e.currentTarget.value)}
          className="input w-4/5 max-w-xs"
        />
      </div>
      <div className="flex flex-col justify-center">
        <label>Number of hosts</label>
        <input
          type="text"
          placeholder="1"
          value={numberOfHosts}
          onChange={(e) => {
            try {
              const newNumberOfHosts = Number.parseInt(e.currentTarget.value);
              if (Number.isNaN(newNumberOfHosts)) return;
              setNumberOfHosts(newNumberOfHosts);
            } finally {
            }
          }}
          className="input w-4/5 max-w-xs"
        />
        <div
          className="node w-2/3 text-lg"
          onDragStart={(event) =>
            onDragStart(event, {
              label: getClusterNameWithDefaults(),
              nodeType: "input",
            })
          }
          draggable
        >
          {getClusterNameWithDefaults()}
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

      <div>
        <button className="btn" onClick={submit}>
          Submit
        </button>
      </div>
    </div>
  );
};

export default Sidebar;
