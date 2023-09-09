using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WKTAAE.DPU.Allocation.Contracts.Dtos.StatementJSON.FIS
{
    public partial class Statement
    {
        public virtual Ulid Id { get; set; }
        public virtual string SourceType { get; set; }      
    }

}
