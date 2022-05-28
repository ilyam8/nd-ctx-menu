# nd-ctx-menu

## Guidelines

* OpenTelemety Metric Semantic Conventions were followed to the best of our understanding (even they seem to have differ   ent approaches in different domains) - https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/semantic_conventions/README.md
   - same metric attributes were purposefully set as part of the context name to better present things to the user, e.g. system.cpu.core.utilization where `core` should be an attribute
* All metrics related to system resources are put under `system` as a root, this implies a merging of System with CPU, Disk, Network, Memory, etc.
* There wasn't (much) of a concern to keep the hierarchy/section levels to a minimum, logic was prioritized against outcome
* Netdata Overview screen with in-section filter capabilities, that will allow to slice the data using attributes attached to the data, as well as, better and easier Custom Dashboard creation/management features are considered to allow better UX
* The revision of contexts won't discard the need of a `dashboard_info.js` (or similar concept) to apply specific adaptions to the menu in specific sections:
   - cgroup metrics need to be divided into the Containers and VMs sections (attribute defines breakdown structure: type)
   - cgroup k8s, docker, etc. metrics will need to be grouped into specific sections 
   - OS specific system metrics will need to be presented in separate OS sections (attribute defines breakdown structure: os)

### Future ideas discussed outside of the scope of this work:
* collectors should provide the following context of a metric (likely more, the gist is to provide a context):
   - applicable/default aggregation methods (e.g. no sense in SUM temperature|network interface duplex|any metric that represents encodes a state (0: running, 1: pending, 2: failed, etc.))
   - applicable/default grouping methods
* key/main metrics, which should be shown per default and an element with (...) would allow user to expand --> user preference could override this
