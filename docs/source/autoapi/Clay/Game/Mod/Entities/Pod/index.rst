
Pod Class
=========



Namespace
    :dn:ns:`Clay.Game.Mod.Entities`

Assemblies
    * Clay.Game

----

.. contents::
   :local:



Inheritance Hierarchy
---------------------

* :dn:cls:`System.Object`
* :dn:cls:`Tuna.Mob`
* :dn:cls:`Clay.Game.Mod.Entities.Entity`
* :dn:cls:`Clay.Game.Mod.Entities.Pod`




Syntax
------

.. code-block:: csharp

    public class Pod : Entity, IComparable, IAudioSourceInfo, ITargettable





.. dn:class:: Clay.Game.Mod.Entities.Pod
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Pod


Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Pod
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Pod.IsOpened



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool IsOpened { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pod.PodId



        :rtype: System.String

        .. code-block:: csharp

            public string PodId { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pod.TargetablePosition



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public override Vector2 TargetablePosition { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pod.TargetableRect



        :rtype: System.Nullable<System.Nullable`1>{UnityEngine.Rect<UnityEngine.Rect>}

        .. code-block:: csharp

            public override Rect? TargetableRect { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pod.activationRange



        :rtype: System.Single

        .. code-block:: csharp

            public static float activationRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Pod.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Pod.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Pod
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Pod.DamagedBy(Clay.Game.Mod.Entities.Entity, System.Single, Weapon, System.Boolean, System.Boolean)



        :type attacker: Clay.Game.Mod.Entities.Entity

        :type damage: System.Single

        :type weapon: Weapon

        :type effectHandled: System.Boolean

        :type fxHandled: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool DamagedBy(Entity attacker, float damage, Weapon weapon, bool effectHandled = false, bool fxHandled = false)

    .. dn:method:: Clay.Game.Mod.Entities.Pod.GetCommandLine(System.Boolean)



        :type multiLine: System.Boolean

        :rtype: System.String

        .. code-block:: csharp

            public override string GetCommandLine(bool multiLine)

    .. dn:method:: Clay.Game.Mod.Entities.Pod.GetRespawnString()



        :rtype: System.String

        .. code-block:: csharp

            public override string GetRespawnString()

    .. dn:method:: Clay.Game.Mod.Entities.Pod.InitialiseLevel()




        .. code-block:: csharp

            public static void InitialiseLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Pod.OutOfHealth()




        .. code-block:: csharp

            public override void OutOfHealth()

    .. dn:method:: Clay.Game.Mod.Entities.Pod.ParentAwakened()




        .. code-block:: csharp

            public override void ParentAwakened()

    .. dn:method:: Clay.Game.Mod.Entities.Pod.ParentColonised()




        .. code-block:: csharp

            public override void ParentColonised()

    .. dn:method:: Clay.Game.Mod.Entities.Pod.PostPopulateLevel()




        .. code-block:: csharp

            public void PostPopulateLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Pod.SpawnPodLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.Pod

        .. code-block:: csharp

            public static Pod SpawnPodLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Pod.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.Pod.Unlock()




        .. code-block:: csharp

            public void Unlock()

    .. dn:method:: Clay.Game.Mod.Entities.Pod.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Pod.ValidateSpawn(System.String[], ref System.String, Clay.Game.Mod.Entities.RespawnRules)



        :type parameters: System.String<System.String>[]

        :type spawnHash: System.String

        :type respawnRule: Clay.Game.Mod.Entities.RespawnRules

        :rtype: System.Boolean

        .. code-block:: csharp

            public static bool ValidateSpawn(string[] parameters, ref string spawnHash, RespawnRules respawnRule)



Fields
------

.. dn:class:: Clay.Game.Mod.Entities.Pod
    :noindex:
    :hidden:

    .. dn:field:: Clay.Game.Mod.Entities.Pod.InitialOpenedPodCount



        :rtype: System.Int32

        .. code-block:: csharp

            public static int InitialOpenedPodCount

    .. dn:field:: Clay.Game.Mod.Entities.Pod.OpenedPodCount



        :rtype: System.Int32

        .. code-block:: csharp

            public static int OpenedPodCount



